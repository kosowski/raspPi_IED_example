
UDPReceiver receiver;

void setup() {
  size(400,400);
  // receiver recibira los mensajes que se envien al puerto 8888
  receiver = new UDPReceiver();
}

void draw() {
  background(255);
  fill(0);
  
  // esperamos hasta que llega un mensaje
 //String data = receiver.receiveData();
 String data ="1250-110";
 println(data);
 
 // extraemos los dos datos, que vienen como texto separados por un '-'
 int positivos = Integer.parseInt( data.substring(0,data.indexOf('-')) );
 int negativos = Integer.parseInt( data.substring(data.indexOf('-')+1) ); 
 int total = positivos + negativos;

 textMode(CENTER);
 
 // dibujamos un :) en la parte izquierda de la pantalla
 //con tamaño proporcional al numero de cometarios positivos
 textSize( 100 * positivos/total);
 text(":)",width/4, height/2);
 
  // dibujamos un :( en la parte derecha de la pantalla
 //con tamaño proporcional al numero de cometarios negativos
 textSize( 100 * negativos/total);
 text(":(", 3*width/4, height/2);
}

