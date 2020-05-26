library fatequino.api;

import 'dart:io';
import 'dart:math';

/** Biblioteca para comunicação com as api do fatequino */

import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert' show Utf8Decoder, json;

bool ligado = false;

 Future<String> sendMensagem({String mensagem}) async {
//  print("$host,$port");
  var apiUrl = Uri.parse('https://fatequino.com.br/chatbot/get?msg='+mensagem);//Uri.parse('${_httpP}://${_host}:${_port}/');
  var client = HttpClient(); // `new` keyword optional

  HttpClientRequest request = await client.getUrl(apiUrl);

//  request.write(mensagem);

  HttpClientResponse response = await request.close();

  var resStream = response.transform(Utf8Decoder());
  await for (var data in resStream) {
    return data;
  }
 }
