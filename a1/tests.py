import course
import survey
import criterion
import grouper
import pytest
from typing import List, Set, FrozenSet


def empty_course() -> course.Course:
    return course.Course('csc148')



def students() -> List[course.Student]:
    return [course.Student(3, 'Gertrude'),course.Student(1, 'Zoro'),
           course.Student(4, 'Yvette'),course.Student(2, 'Aaron')]


def test___str__(self, students) -> None:
    student = students[0]
    assert student.name == student.__str__()


def test_enroll_students(empty_course, students) -> None:
    empty_course.enroll_students(students)
    for student in students:
        assert student in empty_course.students
#
#    def test_all_answered(self, course_with_students_with_answers,
#                          survey_) -> None:
#        assert course_with_students_with_answers.all_answered(survey_)

def test_get_students(course_with_students,empty_course, students) -> None:
#        students = course_with_students.get_students()
#        for student in students:
#            assert student in course_with_students.students
#        for i in students:
#            print('students from get function')
#            print(i.name)
#        for i in course_with_students:
#            print('students from course enrollment')
#
#            print(i.name)
    assert course_with_students.get_students()==\
    [students[1],students[3],students[0],students[2]]


acourse=empty_course()
stu=students()
test_enroll_students(acourse, stu)
for student in acourse.students:
    print(student.id, student.name)
for student in acourse.get_students():
    print(student.id, student.name)

#stu1=stu[0]
#stu1.set_answer(mc, ans)
#stu1.has_answer(mc)
#stu1.has_answer(nq)
#stu1.get_answer(mc)

#-----------question-
mc= survey.MultipleChoiceQuestion(1, 'what price', [4,2,6])
ans= survey.Answer(2)
mc.validate_answer(ans)

ans2 = survey.Answer(4)
mc.validate_answer(ans2)

mc.get_similarity(ans, ans2)

nq=survey.NumericQuestion(2, 'age?', 10, 20)
ans3 = survey.Answer(15)
nq.validate_answer(ans3)

ans4 = survey.Answer(13)
nq.get_similarity(ans3, ans4)
ans4.is_valid(nq)

yesno=survey.YesNoQuestion(3, 'good?')
ans5= survey.Answer(True)
ans6= survey.Answer(False)
yesno.validate_answer(ans5)
yesno.get_similarity(ans5, ans6)

ck= survey.CheckboxQuestion(4, 'food?', ['sushi', 'ham', 'burger'])
ans7=survey.Answer(['sushi', 'hamburger'])
ans8=survey.Answer(['sushi', 'ham', 'burger'])
ans9 =survey.Answer( ['sushi'])
ck.validate_answer(ans7)
ck.validate_answer(ans8)
ck.get_similarity(ans8, ans9)



#-----------criterion------


cr1=criterion.HomogeneousCriterion()
mc= survey.MultipleChoiceQuestion(1, 'why?', ['a', 'b'])
cr1.score_answers(mc, [survey.Answer('a'), survey.Answer('b'),survey.Answer('a'), survey.Answer('b')])

cr2=criterion.HeterogeneousCriterion()
nq=survey.NumericQuestion(2, 'what?', -2, 4)
cr2.score_answers(nq, [survey.Answer(0), survey.Answer(4), survey.Answer(-1), survey.Answer(1)])

cr3=criterion.LonelyMemberCriterion()
yesno=survey.YesNoQuestion(3, 'good?')
cr3.score_answers(nq, [survey.Answer(True), survey.Answer(False), survey.Answer(True),survey.Answer(True)])

ck= survey.CheckboxQuestion(4, 'food?', ['a', 'b', 'c'])
cr1.score_answers(ck, [survey.Answer(['a', 'b']), survey.Answer(['a', 'b']),survey.Answer(['a']), survey.Answer(['b'])])

s = survey.Survey([mc, yesno, nq, ck])

stu[0].set_answer(mc, survey.Answer('a'))
stu[1].set_answer(mc, survey.Answer('b'))
stu[2].set_answer(mc, survey.Answer('a'))
stu[3].set_answer(mc, survey.Answer('b'))

stu[0].set_answer(yesno, survey.Answer(True))
stu[1].set_answer(yesno, survey.Answer(False))
stu[2].set_answer(yesno, survey.Answer(True))
stu[3].set_answer(yesno, survey.Answer(True))

stu[0].set_answer(nq, survey.Answer(0))
stu[1].set_answer(nq, survey.Answer(4))
stu[2].set_answer(nq, survey.Answer(-1))
stu[3].set_answer(nq, survey.Answer(1))

stu[0].set_answer(ck, survey.Answer(['a', 'b']))
stu[1].set_answer(ck, survey.Answer(['a', 'b']))
stu[2].set_answer(ck, survey.Answer(['a']))
stu[3].set_answer(ck, survey.Answer(['b'])) #ans7 is invalid answer try it to raise error

acourse.all_answered(s)
#mc.validate_answer(ans)
#nq.validate_answer(ans4)
#stu[0].has_answer(nq)
#stu[1].has_answer(nq)
#stu[2].has_answer(nq)
#stu[3].has_answer(nq)

s.set_criterion(cr1, mc)
s.set_criterion(cr3, yesno)
s.set_criterion(cr2, nq)
s.set_criterion(cr1, ck)

s.score_students(stu)


#-----group------
group1 = grouper.Group(stu)

g =grouper.Grouping()
g.add_group(group1)
g.get_groups()
stu2= [course.Student(5, 'Rich'),course.Student(6, 'Zoro'),
           course.Student(7, 'Sue'),course.Student(8, 'Aaron')]

group2 = grouper.Group(stu2)
g.add_group(group2)

#print(g)


acourse.enroll_students(stu2)

stu2[0].set_answer(mc, ans)
stu2[1].set_answer(mc, ans)
stu2[2].set_answer(mc, ans)
stu2[3].set_answer(mc, ans)

stu2[0].set_answer(yesno, ans5)
stu2[1].set_answer(yesno, ans5)
stu2[2].set_answer(yesno, ans6)
stu2[3].set_answer(yesno, ans6)

stu2[0].set_answer(nq, ans3)
stu2[1].set_answer(nq, ans4)
stu2[2].set_answer(nq, ans4)
stu2[3].set_answer(nq, ans3)

stu2[0].set_answer(ck, ans8)
stu2[1].set_answer(ck, ans8)
stu2[2].set_answer(ck, ans9)
stu2[3].set_answer(ck, ans8)

acourse.all_answered(s)

#groupping = grouper.AlphaGrouper(3)
#alpha_g = groupping.make_grouping(acourse, s)
#print(alpha_g)
#
#groupping = grouper.RandomGrouper(5)
#rand_g = groupping.make_grouping(acourse, s)
#print(rand_g)


groupping = grouper.GreedyGrouper(4)
greed_g = groupping.make_grouping(acourse, s)
print(greed_g)

#groupping = grouper.WindowGrouper(3)
#window_g = groupping.make_grouping(acourse, s)
#print(window_g)

#
#class TestGreedyGrouper:
#    def test_make_grouping(self, course_with_students_with_answers,
#                           greedy_grouping,
#                           survey_) -> None:
#        grouper_ = grouper.GreedyGrouper(2)
#        grouping = grouper_.make_grouping(course_with_students_with_answers,
#                                          survey_)
#        compare_groupings(grouping, greedy_grouping)
        