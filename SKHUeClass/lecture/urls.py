from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^my_lecture_list$', my_lecture_list, name='my_lecture_list'),
    url(r'^lecture_detail/(?P<lecture_id>[0-9]+)$', lecture_detail, name='lecture_detail'),
    url(r'^lecture_list$', lecture_list, name='lecture_list'),
    url(r'^noticeWrite/(?P<lecture_id>[0-9]+)$', noticeWrite, name='noticeWrite'),
    url(r'^noticeModify/(?P<notice_id>[0-9]+)$', noticeModify, name='noticeModify'),
    url(r'^noticeDelete/(?P<notice_id>[0-9]+)$', noticeDelete, name='noticeDelete'),
    url(r'^noticeView/(?P<notice_id>[0-9]+)$', noticeView, name='noticeView'),
    url(r'^questionWrite/(?P<lecture_id>[0-9]+)$', questionWrite, name='questionWrite'),
    url(r'^questionView/(?P<question_id>[0-9]+)$', questionView, name='questionView'),
    url(r'^questionDelete/(?P<question_id>[0-9]+)$', questionDelete, name='questionDelete'),
    url(r'^commentWrite/(?P<question_id>[0-9]+)$', commentWrite, name='commentWrite'),
    url(r'^assignmentSubmit/(?P<notice_id>[0-9]+)$', assignmentSubmit, name='assignmentSubmit'),
    url(r'^assignmentList/(?P<lecture_id>[0-9]+)$', assignmentList, name='assignmentList'),
    url(r'^assignment/(?P<notice_or_assignment_id>[0-9]+)$', assignment, name='assignment'),
    url(r'^studentList/(?P<lecture_id>[0-9]+)$',studentList, name='studentList'),
    url(r'^team/(?P<lecture_or_team_id>[0-9]+)$', team, name='team'),

]
