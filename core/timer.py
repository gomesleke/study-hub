"""
O objetivo do timer.py é ser o cronometro da aplicação
"""

import time
from storage.json_manager import open_create,save
from core.subject import show_subject

study_time=open_create("time_data") #link com .json
subject=open_create("subject_data")


def time_count(time_sec,time_min,time_hours): #isolamento do tempo + get valores

    time.sleep(1)
    time_sec+=1

    if time_sec==60:
        time_sec=0
        time_min+=1
                    
    if time_min==60:
        time_min=0
        time_hours+=1

    return time_sec,time_min,time_hours


def study_main(): #função principal
    time_sec=0
    time_min=0
    time_hours=0

    start_time=input("Deseja estudar: ").lower()

    if start_time == "sim":

        show_subject()

        indice_study_subject=int(input("\nAssunto (indice): ")) #indice

        print("\nCronômetro iniciado! Pressione Ctrl+C para parar.\n")

        try:
            while True:
                    
                time_sec,time_min,time_hours=time_count(
                    time_sec,time_min,time_hours
                )

                print(f"Tempo de estudo: {time_hours:02d}:{time_min:02d}:{time_sec:02d}", end="\r")

        except KeyboardInterrupt: #ctrl+c
            print(f"\n\nSessão finalizada")

            session={
                "subject":subject[indice_study_subject],
                "hours":time_hours,
                "minutes":time_min,
                "seconds":time_sec,
            }


            study_time.append(session)
            save("time_data",study_time)

            print(f"Total estudado: {session['hours']}h {session['minutes']}min {session['seconds']}s")
            print(subject)
        
    else:
        input("Erro - tente novamente")
        main_timer()


def main_timer():
    study_main()


