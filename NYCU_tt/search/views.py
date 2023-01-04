from django.shortcuts import render
from .models import *
from .filters import CourseFilter
from .forms import *
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    course = Course.objects.all().order_by('-id')
    resp = Response.objects.all().order_by('-id')
    cf = CourseFilter(request.GET, queryset = course)
    
    paginated_filter = Paginator(cf.qs, 10)
    page_number = request.GET.get('page')
    course_page = paginated_filter.get_page(page_number)
    total = paginated_filter.page_range

    context={
        'cf':cf,
        'resp':resp,
        'course_page':course_page,
        'total':total,
    }
    return render(request, "search/home.html", context)

def detail(request, pk):
    detail = Response.objects.get(pk=pk)
    return render(request, 'search/detail.html', context={'detail': detail})

def create(request):
    form1 = RawCourseForm(request.POST or None)
    form2 = RawResponseForm(request.POST or None)
    if form1.is_valid():
        exist = Course.objects.filter(courseName=request.POST['courseName']).filter(professor=request.POST['professor']).filter(semester=request.POST['semester']).filter(college=request.POST['college'])
        if not exist:
            Course.objects.create(**form1.cleaned_data)
            form1 = RawCourseForm()
    if form2.is_valid():
        name = request.POST.get('courseName')
        prof = request.POST.get('professor')
        s = request.POST.get('semester')
        col = request.POST.get('college')
        get_course_id = Course.objects.filter(courseName=name).filter(professor=prof).filter(semester=s).filter(college=col)
        Response.objects.create(course=get_course_id[0], **form2.cleaned_data)
        form2 = RawResponseForm()
    context ={
        'form1' : form1,
        'form2' : form2,
    }
    return render(request, 'search/create.html', context)