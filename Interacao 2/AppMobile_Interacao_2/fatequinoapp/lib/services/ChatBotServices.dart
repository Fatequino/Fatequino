library fatequino.api;

import 'dart:io';

//Biblioteca para comunicação com as api do fatequino 

import 'dart:async';
import 'dart:convert' show Utf8Decoder;

bool ligado = false;

Future<String> sendMensagem({String mensagem}) async {
  var apiUrl = Uri.parse('https://fatequino.com.br/chatbot/get?msg='+mensagem);
  var client = HttpClient(); // `new` keyword optional

  HttpClientRequest request = await client.getUrl(apiUrl);
  HttpClientResponse response = await request.close();

  var resStream = response.transform(Utf8Decoder());
  await for (var data in resStream) {
    return data;
  }
  return "Oops, ocorreu um problema na chamada...";
}
