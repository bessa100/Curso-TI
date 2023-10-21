import cv2
import numpy as np

# Carregue a imagem
imagem = cv2.imread('imagem.png')

# Carregue o modelo YOLO
net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')

# Carregue as classes (coco.names contém os nomes das classes)
with open('coco.names', 'r') as f:
    classes = f.read().strip().split('\n')

# Obtenha camadas de saída
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Converta a imagem para um formato que a YOLO possa usar
altura, largura, canais = imagem.shape
blob = cv2.dnn.blobFromImage(imagem, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

# Passe a imagem pela rede
net.setInput(blob)
outs = net.forward(output_layers)

# Informações de exibição
cores = np.random.uniform(0, 255, size=(len(classes), 3))

# Lista de caixas delimitadoras, confianças e IDs de classe
caixas = []
confiancas = []
ids_classes = []

# Iterar sobre todas as detecções
for out in outs:
    for deteccao in out:
        pontuacoes = deteccao[5:]
        id_classe = np.argmax(pontuacoes)
        confianca = pontuacoes[id_classe]
        if confianca > 0.5:
            # Coordenadas da caixa delimitadora
            centro_x, centro_y, largura, altura = map(int, deteccao[0:4] * [largura, altura, largura, altura])
            topo_esquerdo = (centro_x - largura // 2, centro_y - altura // 2)
            caixa = [topo_esquerdo[0], topo_esquerdo[1], largura, altura]
            caixas.append(caixa)
            confiancas.append(float(confianca))
            ids_classes.append(id_classe)

# Aplicar supressão não máxima para remover detecções redundantes
indices = cv2.dnn.NMSBoxes(caixas, confiancas, 0.5, 0.4)

# Desenhe caixas delimitadoras nas detecções finais
for i in range(len(caixas)):
    if i in indices:
        x, y, w, h = caixas[i]
        label = str(classes[ids_classes[i]])
        cor = cores[ids_classes[i]]
        cv2.rectangle(imagem, (x, y), (x + w, y + h), cor, 2)
        cv2.putText(imagem, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, cor, 2)

# Exiba a imagem com as detecções
cv2.imshow('Detecção de Objetos', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()