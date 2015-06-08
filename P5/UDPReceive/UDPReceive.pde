
UDPReceiver receiver;

void setup() {
  size(400,400);
  receiver = new UDPReceiver();
}

void draw() {
  background(20);
 //String data = receiver.receiveData();
 String data ="125-11";
 println(data);
 int positivos = Integer.parseInt( data.substring(0,data.indexOf('-')) );
 int negativos = Integer.parseInt( data.substring(data.indexOf('-')+1) );
 println(positivos + " ; " + negativos);
 textMode(CENTER);
 
 textSize();
 text(":)",width/4, height/2);
 
 textSize();
 text(":(", 3*width/4, height/2);
}

