import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map, tap } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductoService {

 // private apiUrl = 'http://127.0.0.1:8000/'
 private apiUrl = 'https://ecbooksdjango.onrender.com/'

  constructor(private http: HttpClient) { }

  getProducts(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}producto/productos/`);
  }

  joyotas(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}producto/toptres/`).pipe(
      map(products => {
        // Mapea las rutas de las imágenes para que incluyan la URL base
        return products.map(product => {
          return {
            ...product,
            imagen: `${this.apiUrl}${product.imagen}`,
          };
        });
      })
    );
  }

  postProducto(productoForm: any): Observable<any> {
    return this.http.post(`${this.apiUrl}producto/productos/`, 
      productoForm     
    );
  }
  

  getCategoria(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}producto/categoria/`);
  }
  getGenero(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}producto/generos/`);
  }


  getProducto(id: number): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}producto/productos/${id}/`).pipe(
      map(product => {
        // Mapea la ruta de la imagen para que incluya la URL base
        return {
          ...product,
        
        };
      })
    );
  }

  getProductosPorGenero(generoId: number): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}producto/productos/por-genero/${generoId}/`).pipe(
      map(products => {
        // Mapea las rutas de las imágenes para que incluyan la URL base
        return products.map(product => {
          return {
            ...product,
            imagen: `${this.apiUrl}${product.imagen}`,
          };
        });
      })
    );
  }
}
