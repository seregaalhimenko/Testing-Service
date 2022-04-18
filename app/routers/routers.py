from rest_framework import routers
from app.views import theme, test, question, choice, answer_tracker

router = routers.SimpleRouter()

router.register(r'theme', theme.ThemeViewSet)
router.register(r'test', test.TestViewSet)
router.register(r'question', question.QuestionViewSet)
router.register(r'choice', choice.ChoiceViewSet)
router.register(r'answer', answer_tracker.AnswerViewSet)
