import logging
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_model import Response
from random import choice

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hola! Soy tu asistente de aprendizaje de inglés. ¿Quieres practicar inglés conmigo a través de preguntas y respuestas?"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Puedo ayudarte a practicar inglés a través de preguntas y respuestas. Solo tienes que decir 'Pregúntame algo' y responderé con una pregunta en inglés. Luego, puedes intentar responderla en inglés. También puedo enseñarte vocabulario, gramática y más si lo necesitas."
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class QuestionIntentHandler(AbstractRequestHandler):
    """Handler for Question Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("QuestionIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        questions = [
            "What is the capital of the United States?",
            "How many days are there in a week?",
            "What is the opposite of 'hot'?",
            "Can you name a fruit that grows on trees?"
        ]
        question = choice(questions)
        speak_output = f"{question} Can you answer in English?"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class AnswerIntentHandler(AbstractRequestHandler):
    """Handler for Answer Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AnswerIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        answer = slots["answer"].value
        if check_answer(answer):
            speak_output = "Correct! Good job answering in English."
        else:
            speak_output = "I'm sorry, that's not quite right. Why don't you try again?"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

def check_answer(answer):
    # Implement logic to check if the answer is correct
    answers = {
        "washington, d.c.": True,
        "seven": True,
        "cold": True,
        "apple": True
    }
    return answers.get(answer.lower(), False)

sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(QuestionIntentHandler())
sb.add_request_handler(AnswerIntentHandler())

lambda_handler = sb.lambda_handler()
