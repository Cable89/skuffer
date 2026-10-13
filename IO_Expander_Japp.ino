void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  int proMicroPins[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 15, 16, A0, A1, A2, A3};
  for (int i = 0; i < 16; i++) {
    pinMode(proMicroPins[i], INPUT_PULLUP);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  int proMicroPins[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 15, 16, A0, A1, A2, A3};
  char *pins[] = {"P2","P3","P4","P5","P6","P7","P8","P9","P10","P16","P14","P15","A0","A1","A2","A3"};

  uint8_t pinstate[16] = {0};
  uint8_t oldpinstate[16] = {0};

  while(1){
    for(uint8_t i=0; i<16; i++){
      oldpinstate[i] = pinstate[i];
      pinstate[i] = digitalRead(proMicroPins[i]);
      if(oldpinstate[i] != pinstate[i]){
        Serial.print(pins[i]);
        Serial.print(":");
        Serial.print(pinstate[i]);
        Serial.print('\r');
        Serial.print('\n');
      }
    }
    delay(10);
  }
  

}
