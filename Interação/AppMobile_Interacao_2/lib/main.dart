import 'package:fatequino_app/screen/ChoiceScreen.dart';
import 'package:flutter/material.dart';


void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  /**  Aqui é a raiz da aplicação, onde o app começa.*/
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Fatequino app',
      debugShowCheckedModeBanner: false,
      home: ChoiceScreen(),
    );
  }
}
