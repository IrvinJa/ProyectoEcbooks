import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
 providedIn: 'root'
})
export class BalanceService {

  // private apiUrl = 'http://127.0.0.1:8000/'
  private apiUrl = 'https://ecbooksdjango.onrender.com'

 constructor(private http: HttpClient) { }

 getHistorial(balanceId: number): Observable<any[]> {
   return this.http.get<any[]>(`${this.apiUrl}balance/balances/${balanceId}/historial/`);
 }

}