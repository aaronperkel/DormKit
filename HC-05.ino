/*
HC_05.ino
DORMKIT V1.0
*/

int led = 13; // use to check if it's working
// for project, led will be micro torque servo or high torque servo

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop() {
 // put your main code here, to run repeatedly:

  if (Serial.available()) {
    int a = Serial.parseInt(); // will be serial value sent by rasp-pi
    Serial.println(a); // print serial value

    if (a == 100) {
      digitalWrite(led, HIGH);
    }
    if (a == 200) {
      digitalWrite(led, LOW);
    }

    if (a = 300) {
      lightOn();
    }
    if (a = 400) {
      lightOff();
    }

    if (a = 500) {
      lock();
    }
    if (a = 600) {
      unlock();
    }
  }

}
