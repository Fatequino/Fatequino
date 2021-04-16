#define RightMotorForward 7
#define RightMotorBackward 6
#define LeftMotorForward 5
#define LeftMotorBackward 4
#define sensorL A0
#define sensorR A1
#define FW 55
#define TR 70
#define PAUSE 100
 
void setup(){
pinMode(RightMotorForward, OUTPUT);
pinMode(LeftMotorForward, OUTPUT);
pinMode(LeftMotorBackward, OUTPUT);
pinMode(RightMotorBackward, OUTPUT);
pinMode(sensorL,INPUT);
pinMode(sensorR,INPUT);
Serial.begin(9600);
}
 
void loop(){
int left = analogRead(sensorL);
int right = analogRead(sensorR);
Serial.print("Leitura de luminosidade sensor L: ");
Serial.println(left);
Serial.print("Leitura de luminosidade sensor R: ");
Serial.println(right);
if (left > 100 && right > 100){
moveForward();
}
else if (left < 100){
turnLeft();
}
else if (right < 100){
turnRight();
}
delay(PAUSE);
}
 
void moveForward(){
motorLForward();
motorRForward();
delay(FW);
moveStop();
}
 
void turnRight(){
Serial.println("Vira à direita");
motorLForward();
delay(TR);
moveStop();
}
 
void turnLeft(){
Serial.println("Vira à esquerda");
motorRForward();
delay(TR);
moveStop();
}
 
void moveStop(){
digitalWrite(RightMotorForward, LOW);
digitalWrite(LeftMotorForward, LOW);
digitalWrite(RightMotorBackward, LOW);
digitalWrite(LeftMotorBackward, LOW);
}
 
void motorRForward(){
digitalWrite(RightMotorForward, HIGH);
digitalWrite(RightMotorBackward, LOW);
}
 
void motorRBackward(){
digitalWrite(RightMotorForward, LOW);
digitalWrite(RightMotorBackward, HIGH);
}
 
void motorLForward(){
digitalWrite(LeftMotorForward, HIGH);
digitalWrite(LeftMotorBackward, LOW);
}
 
void motorLBackward(){
digitalWrite(LeftMotorForward, LOW);
digitalWrite(LeftMotorBackward, HIGH);
}
