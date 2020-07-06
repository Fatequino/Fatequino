# Code adapted from Passos, Bianka (2019).
# Program to recognize alphabet signs from LIBRAS developed for PDI class.
# Retrieved from: https://github.com/biankatpas/Libras
# Adapted by: Group Fatequino

import cv2
import numpy as np
import math
import time
from _datetime import datetime

# Define put text font
font = cv2.FONT_HERSHEY_SIMPLEX
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
record = cv2.VideoWriter('output/' + str(datetime.now()) + '.avi', fourcc, 20.0, (640, 480))


def main():
    # Capture from webcam
    cam = cv2.VideoCapture(0)
    fgbg = cv2.createBackgroundSubtractorMOG2()

    while True:

        ret, frame = cam.read()

        if ret is False:
            return

        # MOstrar retângulo de ROI
        cv2.rectangle(frame, (20, 20), (300, 300), (255, 255, 2), 4)  # retângulo mais externo
        ROI = frame[20:300, 20:300]

        # Segmentação da mão por movimento
        # Subtração de fundo MOG2
        fgmask = ROI
        fgbg.setBackgroundRatio(0.005)
        fgmask = fgbg.apply(ROI, fgmask)
        # Remoção de ruído
        kernel = np.ones((5, 5), np.uint8)
        c1 = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
        c2 = cv2.morphologyEx(c1, cv2.MORPH_CLOSE, kernel)
        closing = cv2.morphologyEx(c2, cv2.MORPH_CLOSE, kernel)

        # Encontre contornos do quadro filtrado
        contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # print(contours)

        # Desenhar contornos
        for cnt in contours:
            color = [222, 222, 222]  # contours color
            cv2.drawContours(ROI, [cnt], -1, color, 3)

        if contours:

            cnt = contours[0]

            # Encontre momentos do contorno
            moments = cv2.moments(cnt)

            cx = 0
            cy = 0
            # Massa central de momentos de primeira ordem
            if moments['m00'] != 0:
                cx = int(moments['m10'] / moments['m00'])  # cx = M10/M00
                cy = int(moments['m01'] / moments['m00'])  # cy = M01/M00

            center = (cx, cy)

            # Desenhar massa central
            cv2.circle(ROI, center, 15, [0, 0, 255], 2)

            # Encontre o círculo que cobre completamente o objeto com a área mínima
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            center = (int(x), int(y))
            radius = int(radius)
            cv2.circle(ROI, center, radius, (0, 0, 0), 3)
            area_of_circle = math.pi * radius * radius

            # Retângulo delimitador desenhado com área mínima, também considera a rotação
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(ROI, [box], 0, (0, 0, 255), 2)

            # aproximar a forma
            cnt = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)

            # Encontrar defeitos convexos
            hull = cv2.convexHull(cnt, returnPoints=False)
            defects = cv2.convexityDefects(cnt, hull)

            fingers = 0

            # Obter pontos de defeito e desenhar na imagem original
            if defects is not None:
                # print('defects shape = ', defects.shape[0])
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    start = tuple(cnt[s][0])
                    end = tuple(cnt[e][0])
                    far = tuple(cnt[f][0])
                    cv2.line(ROI, start, end, [0, 255, 0], 3)
                    cv2.circle(ROI, far, 8, [211, 84, 0], -1)
                    #  finger count
                    a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                    b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                    c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                    angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  # teorema do cosseno
                    area = cv2.contourArea(cnt)

                    if angle <= math.pi / 2:  # ângulo inferior a 90 graus, tratar como dedos
                        fingers += 1
                        cv2.circle(ROI, far, 1, [255, 0, 0], -1)

                    if len(cnt) >= 5:
                        (x_centre, y_centre), (minor_axis, major_axis), angle_t = cv2.fitEllipse(cnt)

                    letter = ''
                    if area_of_circle - area < 5000:
                        #  print('A')
                        letter = 'A'
                    elif angle_t > 120:
                        letter = 'U'
                    elif area > 120000:
                        letter = 'B'
                    elif fingers == 1:
                        if 40 < angle_t < 66:
                            # print('C')
                            letter = 'C'
                        elif 20 < angle_t < 35:
                            letter = 'L'
                        else:
                            letter = 'V'
                        #print ('Olá aluno!')
                    elif fingers == 2:
                        if angle_t > 100:
                            letter = 'F'
                        # print('W')
                        else:
                            letter = 'W'
                    elif fingers == 3:
                        # print('4')
                        letter = '4'
                    elif fingers == 4:
                        # print('Ola!')
                        letter = 'Ola!'
                    else:
                        if 169 < angle_t < 180:
                            # print('I')
                            letter = 'I'
                        elif angle_t < 168:
                            # print('J')
                            letter = 'J'
                        print ('Olá aluno!')    

        else:
            # imprime mensagem: nenhuma mão detectada
            cv2.putText(frame, "No hand detected", (45, 450), font, 2, np.random.randint(0, 255, 3).tolist(), 2)

        # Mostrar imagens de saídas
        cv2.imshow('frame', frame)
        #cv2.imshow('blur', blur)
        #cv2.imshow('hsv', hsv)
        #cv2.imshow('thresh', thresh)
        cv2.imshow('mog2', fgmask)
        cv2.imshow('ROI', ROI)

        record.write(frame)

        # Verifica a tecla pressionada
        if cv2.waitKey(100) == 27:
            break  # ESC para sair

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
