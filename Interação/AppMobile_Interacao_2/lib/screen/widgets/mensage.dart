import 'package:flutter/material.dart';
import 'package:fatequino_app/screen/style.dart' as style;

class Mensagem extends StatelessWidget {
  /** Widget de mensagem */
  Mensagem({Key key, this.mensagem, this.minha = false});
  String mensagem;
  bool minha;

  @override
  Widget build(BuildContext context) {
    return Align(
      alignment: this.minha ? Alignment.topRight : Alignment.topLeft,
      child: Container(
        color: style.colorPrimary,
        width: MediaQuery.of(context).size.width * 0.5,
        margin: EdgeInsets.all(5),
        padding: EdgeInsets.all(5),
        child: Text(
          "${this.mensagem}",
          style: TextStyle(color: Colors.black, fontSize: 20),
        ),
      ),
    );
  }
}