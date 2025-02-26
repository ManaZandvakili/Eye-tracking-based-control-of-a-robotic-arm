import controlP5.*;
import processing.serial.*;
int i;
Serial port;
ControlP5 cp5;
PFont font;
void setup() {
    size(1290,980);  //window size
font=createFont("Times New Roman Bold", 80);
printArray(Serial.list());  //prints all available serial ports
port=new Serial(this, "COM3", 9600);
cp5=new ControlP5(this);
  cp5.addButton("A")
   .setPosition(30,200)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("B")
   .setPosition(190,200)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("C")
   .setPosition(350,200)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("D")
   .setPosition(510,200)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("E")
   .setPosition(670,200)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("F")
   .setPosition(830,200)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("G")
   .setPosition(990,200)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("H")
   .setPosition(1150,200)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("I")
   .setPosition(30,360)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("J")
   .setPosition(190,360)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("K")
   .setPosition(350,360)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("L")
   .setPosition(510,360)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("M")
   .setPosition(670,360)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("N")
   .setPosition(830,360)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("O")
   .setPosition(990,360)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("P")
   .setPosition(1150,360)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("Q")
   .setPosition(30,520)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("Q")
   .setPosition(30,520)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("R")
   .setPosition(190,520)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("S")
   .setPosition(350,520)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("T")
   .setPosition(510,520)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("U")
   .setPosition(670,520)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("V")
   .setPosition(830,520)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("W")
   .setPosition(990,520)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("X")
   .setPosition(1150,520)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("Y")
   .setPosition(510,680)
   .setSize(120,120)
   .setFont(font)
   ;
  cp5.addButton("Z")
   .setPosition(670,680)
   .setSize(120,120)
   .setFont(font)
   ;
}
void draw(){
  background(214,236,240);
  fill(0,33,95);
  text("Keyboard",470,100);
  textSize(128);
  textFont(font);
}
void O(){
  port.write('o');
}
void T(){
  port.write('t');
}
void I(){
  port.write('i');
}
