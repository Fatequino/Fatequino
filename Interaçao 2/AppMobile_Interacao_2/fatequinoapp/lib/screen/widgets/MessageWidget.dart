import 'package:flutter/material.dart';
import 'package:fatequino_app/helper/Style.dart' as style;

//import 'package:flutter_custom_clippers/flutter_custom_clippers.dart';


enum TipoMensagem {
    enviando,
    recebendo
}


class MensagemEnviada extends StatelessWidget{
  MensagemEnviada({Key key, this.mensagem});
  final String mensagem;
  final Color foreground = Colors.black;
  final Color background = style.colorPrimary;

  Widget build(BuildContext context){
    return Mensagem(
        messageText: mensagem, 
        foregroundColor: foreground,
        backgroundColor: background, 
        side: "right"
        );
  }
}

class MensagemRecebida extends StatelessWidget{
  MensagemRecebida({Key key, this.mensagem});
  final String mensagem;
  final Color foreground = Colors.black;
  final Color background = Color(0xFFC0CCC7);
  //@override
  Widget build(BuildContext context){
    return Mensagem(
        messageText: mensagem, 
        foregroundColor: foreground,
        backgroundColor: background, 
        side: "left"
        );
  }
  
}

class Mensagem extends StatelessWidget {
  //Widget de mensagem 
  Mensagem({Key key, this.messageText, this.foregroundColor, this.backgroundColor, this.side});
 
  final String messageText;
  final String side;
  final Color foregroundColor;
  final Color backgroundColor;

  @override
  Widget build(BuildContext context) {
    var now = new DateTime.now();
    String dataFormatada = "${now.hour}:${now.minute}";
    return Align(
      alignment: side == "right" ? Alignment.topRight : Alignment.topLeft,
      
      child: Container(
        margin: EdgeInsets.fromLTRB(0, 5, 0, 5),
        child:
        ClipRRect(
          borderRadius: side == "right" ? BorderRadius.only(topLeft:  Radius.circular(12), bottomLeft: Radius.circular(12)): BorderRadius.only(topRight:  Radius.circular(12), bottomRight: Radius.circular(12)),
          child: 
            Container(
              constraints: BoxConstraints(minWidth: 100, maxWidth: MediaQuery.of(context).size.width * 0.75),
              color: backgroundColor,
              padding: EdgeInsets.all(10),
              child: Column(
                children: <Widget>[
                  Text(this.messageText,
                    style: TextStyle(
                    color: foregroundColor,
                    fontSize: 15
                    ),
                  ),
                  Text (dataFormatada,
                      textAlign: TextAlign.right,
                      style: TextStyle(
                        color: foregroundColor,
                        fontSize: 8
                      ),
                    )
                ],
              )
            ),
          ) 
      ,)
    );
  }
}
