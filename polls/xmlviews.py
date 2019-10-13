import os
from polls.views import parseStandardsXml, scheduleHtml, schedulelistHtml, syllabiXmlHTML, \
    scheduleTeachingAssignmentHtml


##All of these def's return a HttpResponse. They are not sent to a template

# finds acm-cs.xml file. Called from urls.py
def parStandards(request):
    path = 'curriculum/mwsu_curriculum/standards/'
    for filename in os.listdir(path):
        if not filename.endswith('acm-cs.xml'): continue
        fullname = os.path.join(path, filename)
        xml = parseStandardsXml(request, fullname)
    return xml


# finds mwsu-cs-schedule-sp19.xml file. Called from urls.py
def parSchedule(request, schedule):
    path = 'curriculum/mwsu_curriculum/schedules/'
    for filename in os.listdir(path):
        if not filename.endswith(schedule + '.xml'): continue
        fullname = os.path.join(path, filename)
        print(fullname)
        xml = scheduleHtml(request)
    return xml


def parTeachingAssignment(request, schedule):
    path = 'curriculum/mwsu_curriculum/schedules/'
    for filename in os.listdir(path):
        if not filename.endswith(schedule + '.xml'): continue
        fullname = os.path.join(path, filename)
        print(fullname)
        xml = scheduleTeachingAssignmentHtml(request)
    return xml


# finds the requested course xml file. Called from urls.py
def parCourses(request, course):
    path = 'curriculum/mwsu_curriculum/syllabi/'
    for filename in os.listdir(path):
        if not filename.endswith(course + '.xml'): continue
        fullname = os.path.join(path, filename)
        print("giving this one " + filename)
        xml = syllabiXmlHTML(request, fullname)
    return xml
