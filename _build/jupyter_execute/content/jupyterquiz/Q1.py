#!/usr/bin/env python
# coding: utf-8

# # Quiz 1

# In[1]:


from jupyterquiz import display_quiz

q1=[{
            "question": "Warum benötigt man ein einheitliches Einheitensystem?",
            "type": "multiple_choice",
            "answers": [
                {
                    "answer": "Um internationale Kooperation zu erleichtern",
                    "correct": True,
                    "feedback": "Richtig, jeder König benutzt nicht mehr seine eigenen Körperteile um Länge zu definieren."
                },
                {
                    "answer": "Es erhöht das Risiko von Fehlern und Unfällen",
                    "correct": False,
                    "feedback": "Falsch."
                },
                {
                    "answer": "Es vereinfacht den Prozess der Normung und Standardisierung von Produkten, Bauteilen und Messverfahren",
                    "correct": True,
                    "feedback": "Richtig."
                },
                {
                    "answer": "Es verhindert, dass Messfehler entstehen und weltweit unverfälschte Werte gemessen werden.",
                    "correct": False,
                    "feedback": "Falsch. Messfehler passieren trotzdem."
                }
            ]
    }]

q2=[{
            "question": "Wofür steht die Abkürzung SI?",
            "type": "multiple_choice",
            "answers": [
                {
                    "answer": "Système International d'Unités",
                    "correct": True,
                    "feedback": "Richtig, was übersetzt Internationales Einheitensystem bedeutet."
                },
                {
                    "answer": "Standardisierte Internationale Einheiten",
                    "correct": False,
                    "feedback": "Falsch."
                }
            ]
    }]

q3=[{
            "question": "Wie viele Basiseinheiten gibt es?",
            "type": "many_choice",
            "answers": [
                {
                    "answer": "3",
                    "correct": False,
                    "feedback": "Falsch."
                },
                {
                    "answer": "5",
                    "correct": False,
                    "feedback": "Falsch."
                },
                {
                    "answer": "7",
                    "correct": True,
                    "feedback": "Richtig."
                },
                {
                    "answer": "9",
                    "correct": False,
                    "feedback": "Falsch."
                }
            ]
    }]
q4=[{
            "question": "Welches sind die Basiseinheiten im SI-System?",
            "type": "many_choice",
            "answers": [
                {
                    "answer": "Sekunde (s)",
                    "correct": True,
                    "feedback": "Richtig, für die Zeit."
                },
                {
                    "answer": "Volt (V)",
                    "correct": False,
                    "feedback": "Falsch."
                },
                {
                    "answer": "Candela (cd)",
                    "correct": True,
                    "feedback": "Richtig, für die Lichtstärke."
                },
                {
                    "answer": "Gramm (g)",
                    "correct": False,
                    "feedback": "Falsch."
                },   
                {
                    "answer": "mol",
                    "correct": True,
                    "feedback": "Richtig, für die Stoffmenge."
                },
                                {
                    "answer": "Ampere (A)",
                    "correct": True,
                    "feedback": "Richtig, für die Stromstärke."
                },
                                {
                    "answer": "Kilogramm (kg)",
                    "correct": True,
                    "feedback": "Richtig, für die Masse."
                },
                                {
                    "answer": "Kelvin (K)",
                    "correct": True,
                    "feedback": "Richtig, für die Temperatur."
                },               
                {
                    "answer": "Meter (m)",
                    "correct": True,
                    "feedback": "Richtig, für die Länge."
                },
                {
                    "answer": "Radian (rad)",
                    "correct": False,
                    "feedback": "Falsch."
                },
            ]
    }]


# In[2]:


display_quiz(q1, colors='fdsp')
display_quiz(q2, colors='fdsp')
display_quiz(q3, colors='fdsp')
display_quiz(q4, colors='fdsp')


# In[ ]:




