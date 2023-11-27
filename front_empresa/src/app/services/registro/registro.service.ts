import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class RegistroService {
  // private apiUrl = 'http://127.0.0.1:8000/'
  private apiUrl = 'https://ecbooksdjango.onrender.com'

  constructor(private http: HttpClient) { }

  registro(registroForm: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/usuario/api/registro/`, 
      registroForm     
    );
  }

   obtenerUsuario(id: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/usuario/api/verusuario/${id}/`);
  }
}
