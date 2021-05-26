//definicao valores de variaveis globais
#define RightMotorForward 7
#define RightMotorBackward 6
#define LeftMotorForward 5
#define LeftMotorBackward 4
#define sensorL A0
#define sensorR A1
#define FW 55
#define TR 70
#define PAUSE 100
 
//constantes e variaveis dos sensores ultrasonicos
//valores dos pinos dos sensores
const int ultra_left = 6;
const int ultra_front = 7;
const int ultra_right = 8;
const int sensor_left = 9;
const int sensor_front = 10;
const int sensor_right = 11;

//variaveis que armazenarão o cálculo dos centímetros de distancia dos sensores
int cm_left = 0; //sensor da esquerda
int cm_front = 0; //sensor frontal
int cm_right = 0; //sensor da direita

//variaveis que receberam dados dos sensores
bool valor_sensor_left = 0; 
bool valor_sensor_front = 0; 
bool valor_sensor_right = 0; 

//variaveis para calibragem
int distancia_minima = 50;

//Inicializa portas de entrada e saida arduino 
void setup(){
    //atribui pinos dos motores
    pinMode(RightMotorForward, OUTPUT);
    pinMode(LeftMotorForward, OUTPUT);
    pinMode(LeftMotorBackward, OUTPUT);
    pinMode(RightMotorBackward, OUTPUT);
    
    //atribui pinos dos sensores infravermelhos(linha)
    pinMode(sensorL,INPUT);
    pinMode(sensorR,INPUT);
    
    //atribui pinos dos sensores ultrasonicos
    pinMode(ultra_left, INPUT);
    pinMode(ultra_front, INPUT);
    pinMode(ultra_right, INPUT);
  
    Serial.begin(9600);
}


//loop principal de inicialização do arduino
void loop(){

    //leitura de valores sensores luminosidade esquerdo e direto
    int left = analogRead(sensorL);
    int right = analogRead(sensorR);

    Serial.print("Leitura de luminosidade sensor L: ");
    Serial.println(left);
    Serial.print("Leitura de luminosidade sensor R: ");
    Serial.println(right);

    //Realiza o cálculo da distancia de cada sensor ultrasonico
    cm_left = 0.01723 * readUltrasonicDistance(6);
    cm_front = 0.01723 * readUltrasonicDistance(7);
    cm_right = 0.01723 * readUltrasonicDistance(8);

    //logica movimentação robo
    
    //checa se existem obstaculos detectados pelos sensores ultrasonicos a menos de 10 cm de distancia
    //passa para a checagem dos sensores infravermelhos apenas se satisfizer a condicao
    //caso valores recebido por sensores maior que cem em ambos, move para frente
    //valor recebido sensor esquerda menor que cem, move para esquerda
    //valor recebido sensor direita menor que cem, move para direita
    if int cm_left > 10 || int cm_front > 10 || int cm_right > 10{
      if (left > 100 && right > 100){
          moveForward();
      }else if (left < 100){
          turnLeft();
      }else if (right < 100){
          turnRight();
      }
    }
    
    //pausa de 100 milisegundos no loop
    delay(PAUSE);
}

//funcão movimentação para frente
void moveForward(){
    motorLForward();
    motorRForward();
    delay(FW);
    moveStop();
}

//funcao movimentação para esquerda
void turnLeft(){
    Serial.println("Vira à esquerda");
    motorRForward();
    delay(TR);
    moveStop();
}

//funcão movimentação para direita
void turnRight(){
    Serial.println("Vira à direita");
    motorLForward();
    delay(TR);
    moveStop();
}

//funcão para ativar motor esquerdo 
void motorLForward(){
    digitalWrite(LeftMotorForward, HIGH);
    digitalWrite(LeftMotorBackward, LOW);
}

//funcão para ativar motor direito
void motorRForward(){
    digitalWrite(RightMotorForward, HIGH);
    digitalWrite(RightMotorBackward, LOW);
}

//funcao desativar ambos motores 
void moveStop(){
    digitalWrite(RightMotorForward, LOW);
    digitalWrite(LeftMotorForward, LOW);
    digitalWrite(RightMotorBackward, LOW);
    digitalWrite(LeftMotorBackward, LOW);
}

long readUltrasonicDistance(int pin)
{
  pinMode(pin, OUTPUT);  // Clear the trigger
  digitalWrite(pin, LOW);
  delayMicroseconds(2);
  // Sets the pin on HIGH state for 10 micro seconds
  digitalWrite(pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(pin, LOW);
  pinMode(pin, INPUT);
  // Reads the pin, and returns the sound wave travel time in microseconds
  return pulseIn(pin, HIGH);
}
