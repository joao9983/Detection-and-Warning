import cv2
import time
# Utilizando a YoloV4 - pesos já treinados
import requests

url = "http://192.168.3.57:5001/test"


# class colors
COLORS = [(0,255,255),(255,255,0),(0,255,0),(255,0,0)]

# carregar as classes
with open("classes.names","r") as file:
    class_names = [coconames.strip() for coconames in file.readlines()]

# captura de vídeo
capture = cv2.VideoCapture("rtsp://admin:lapisco2021@200.129.48.40:10025/cam/realmonitor?channel=1&subtype=0")
#capture = cv2.VideoCapture(0)

# Carregar Pesos da rede neural
net = cv2.dnn.readNet("pesos/yolov4-tiny.weights", "pesos/yolov4-tiny.cfg")
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)

# Setar parâmetros da rede neural
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416,416), scale = 1/255,swapRB=True)

# Ler os frames do vídeo
while True:
    # Captura do frame
    _,frame = capture.read()
    if not _:
        exit()

    #Inicio da contagem de tempo
    start = time.time()

    # Detecção
    classes, scores, boxes = model.detect(frame,0.2,0.4)

    # Fim da contagem do tepmo
    end = time.time()
    
    flag = 0
    
    

    # Percorrer detecções
    for(classId, score,box) in zip(classes,scores,boxes):

        # Gerar cor para cada classe
        color = COLORS[int(classId)%len(COLORS)]

        # Obtendo nome da classe pelo seu respectivo ID
        label = "%s : %f" % (class_names[classId], score)
        
        
        labelName = label.split(':')[0]

            #print(labelName)
        
        labelName = labelName.strip()
        
        if str(labelName)  == 'person' : 

                #print(frame)

            # Desenhar a box detectada
            cv2.rectangle(frame,box,color,2)

            # Escrever o nome da classe em cima da box do objeto
            cv2.putText(frame,label,(box[0],box[1]-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,color,2)

            # Calcular o tempo levado para a detecção
            fps_label = f"FPS:{round((1.0/(end-start)),2)}"

            # Escrever fps na imagem
            cv2.putText(frame,fps_label,(0,25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),5)
            
            cv2.putText(frame,fps_label,(0,25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
             
            url = "http://192.168.3.57:5001/led?status=on"
            response = requests.get(url)
            print("fds")
            if response.status_code == 200:
                    print(response.text)
            else:
                    print("Erro na requisição: código de status " + str(response.status_code))
    
                     
            
             
        else : #aqui a chama a função q desliga o led (não há pessoa detectada)
                
            print("Not a person ")        
            url = "http://192.168.3.57:5001/led?status=off"
            response = requests.get(url)
                    
            if response.status_code == 200:
                print(response.text)
            else:
                print("Erro na requisição: código de status " + str(response.status_code))
    
                print("PESSOA PESSOA PESSOA - LIGAR LED") 
                
                
   


   