import 'package:fatequino_app/screen/ChatScreen.dart';
import 'package:flutter/material.dart';
import 'package:fatequino_app/helper/Style.dart' as style;

class ChoiceScreen extends StatelessWidget {
  //Tela de escolha da comunicação (Wifi) 
  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        appBar: AppBar(
          backgroundColor: style.colorPrimary,
          title: Text(
            "FATEQUINO :)",
            style: TextStyle(
              color: Colors.black,
            ),
          ),
          centerTitle: true,
        ),
        backgroundColor: style.colorSecondary,
        body: Container(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: <Widget>[
              Container(
                margin: EdgeInsets.all(10),
                alignment: Alignment.center,
                child: Text(
                  "Conversa com \n\t\t\to fatequino: ",
                  style: TextStyle(color: Colors.white, fontSize: 30),
                  maxLines: 2,
                  
                ),
              ),
              Container(
                margin: EdgeInsets.all(5),
                child: IconButton(
                  onPressed: () {//inicia o chat para a web (api de chatbot)
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => ChatScreen(),
                      ),
                    );
                  },
                  icon: Icon(Icons.wifi),
                  color: Colors.white,
                ),
                color: style.colorPrimary,
              ),
              Container(
                margin: EdgeInsets.all(10),
                child: Text(
                  "Web",
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 30,
                  ),
                ),
              ),
              Container(
                child: Text(
                  "Versão 0.20",
                  style: TextStyle(color: Colors.white),
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
