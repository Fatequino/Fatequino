define pinLED 10

void setup(){
pinMode(pinLED, OUTPUT);
Serial.begin(9600);
}

void loop(){

if(serial.available()){
char status = char(Serial.read());

  if(status == '0'){
      digitalWrite(pinLED, LOW);
  }

  if(status == '1'){
    digitalWrite(pinLED, HIGH);
  }    
}

}
