import processing.net.*;
import java.io.*;
import java.net.*;
import java.util.*;
//Server myServer;

class UDPReceiver{
DatagramSocket serverSocket;

byte[] receiveData;

UDPReceiver(){
   try {
    serverSocket = new DatagramSocket(8888);
  }
  catch (IOException e) {
    e.printStackTrace();
    System.out.println(e);
  }

  receiveData = new byte[500];
}

public String receiveData(){
   try {
    DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
    serverSocket.receive(receivePacket);
    String data = new String(receivePacket.getData());
    return data;
  }
  catch (IOException e) {
    return (e.getMessage());
  }
  
}
}
