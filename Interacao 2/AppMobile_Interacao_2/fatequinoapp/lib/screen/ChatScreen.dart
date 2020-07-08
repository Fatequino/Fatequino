import 'package:fatequino_app/screen/widgets/MessageWidget.dart';
import 'package:flutter/material.dart';
import 'package:fatequino_app/helper/Style.dart' as style;
import 'package:fatequino_app/services/ChatBotServices.dart' as api;

class ChatScreen extends StatefulWidget {
  //Tela do chat
  @override
  State<StatefulWidget> createState() {
    return _ChatScreen();
  }
}

class _ChatScreen extends State<ChatScreen> {
  static TextEditingController txt = TextEditingController();
  static FocusNode _focusNode = new FocusNode();
  static List<Widget> _chatMessageWidgets = [];


  static Color _chatBackgroundColor = style.colorSecondary;
  static Color _chatInputTextColor = Color(0xFFC1C9CE);
  static Color _chatInputHintColor = Colors.grey;
  static Color _chatInputBackgroundColor = Color(0xFF2D383E);
  
  //static Color hintColor = lightGray;
  String _currentMessage = "";
  bool waitingMessage = false;

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        appBar: AppBar(
          titleSpacing: 0,
          //leading: Icon(Icons.menu),
          backgroundColor: style.colorPrimary,
          title: Stack(
            children: <Widget>[
              Row(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: <Widget>[
                  CircleAvatar(
                    backgroundColor: style.colorSecondary,
                    child: Text('FQ'),
                  ),
                  Text("  Fatequino",style: TextStyle(color: style.colorSecondary)),
                ]
                ),
            ],
          ),
          centerTitle: true,
        ),
        backgroundColor: _chatBackgroundColor,
        body: Column(
          children: <Widget>[
            Expanded(
              child: SingleChildScrollView(
                reverse: true,
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.start,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: _chatMessageWidgets,
                ),
              ),
            ),
            SingleChildScrollView(
              child: Container(
                  margin: EdgeInsets.all(5),
                  color: _chatBackgroundColor,
                  child: Form(
                    child: TextFormField(
                      onChanged: (e) {
                        setState(() {
                          _currentMessage = e;
                        });
                      },
                      maxLines: 3,
                      minLines: 1,
                      controller: txt,
                      focusNode: _focusNode,
                      cursorColor: style.colorSecondary,
                      keyboardType: TextInputType.multiline,
                      style: TextStyle(
                        color: _chatInputTextColor
                      ),
                      decoration: InputDecoration(
                        
                        hintText: 'Digite uma mensagem',
                        hintStyle: TextStyle(color: _chatInputHintColor),
                        filled: true,
                        fillColor: _chatInputBackgroundColor,
                        contentPadding: EdgeInsets.symmetric(vertical: 5, horizontal: 20),
                        enabledBorder: OutlineInputBorder(
                          
                          borderRadius: BorderRadius.all(Radius.circular(30.0)),
                          borderSide: BorderSide(color: Colors.grey, width: 2),
                        ),
                        focusedBorder: OutlineInputBorder(
                          borderRadius: BorderRadius.all(Radius.circular(30.0)),
                          //borderSide: BorderSide(color: style.secundaryColor, width: 2),
                        
                        ),
                        suffixIcon: sendMensagemButton(),
                      ),
                      // decoration: InputDecoration(
                      //   border: OutlineInputBorder(),
                      //   suffixIcon: sendMensagemButton(),
                      //   //prefixIcon: audiobutton(),
                      // ),
                    ),
                  )),
            ),
          ],
        ),
      ),
    );
  }

  Widget sendMensagemButton() {
    /** Widget do botão de enviar mensagem */
    
    return IconButton(
      icon: Icon(Icons.send),
      color: style.colorPrimary,
      // onPressed: _currentMessage.trim().isNotEmpty ? () {
      //     Widget userMessage;
      //     Widget fatequinoMessage;
      //     userMessage = MensagemEnviada(mensagem: _currentMessage);
      //     fatequinoMessage = MensagemRecebida(mensagem: "Oi, como vc está?");
      //     setState(() {
      //       _chatMessageWidgets.add(userMessage);
      //       _chatMessageWidgets.add(fatequinoMessage);
      //       cleanInput();
      //     });
      // } : null
      onPressed: _currentMessage.trim().isNotEmpty && this.waitingMessage == false
          ? () {
                String messageSent = _currentMessage;
                cleanInput();
                this.waitingMessage = true;
                //if para escolher se app esta no modo teste ou ele envia algo para api 
                api.sendMensagem(mensagem: this._currentMessage.trim()).then((value) {
                  Widget meu;
                  Widget fatequino;
                  meu = MensagemEnviada(mensagem: messageSent);
                  fatequino = MensagemRecebida(mensagem: value);
                  setState(() {
                    _chatMessageWidgets.add(meu);
                    _chatMessageWidgets.add(fatequino);
                    cleanInput();
                  });
                  this.waitingMessage = false;
                }).catchError((erro) {
                  print(erro.toString());
                  this.waitingMessage = false;
                });
                
              }
          : null,
     );
  }

  void cleanInput() async {
    /** Função para limpa o campo de input quando a mensagem é enviada */
    Future.delayed(Duration(milliseconds: 100), () {
      this.setState(() {
        txt.clear();
        this._currentMessage = "";
      });
    });
  }
}