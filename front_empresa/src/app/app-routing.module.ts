import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './paginas/login/login.component';
import { InicioComponent } from './paginas/inicio/inicio.component';
import { ContactoComponent } from './paginas/contacto/contacto.component';
import { RegistroComponent } from './paginas/registro/registro.component';

const routes: Routes = [

 
 {path:'login',component:LoginComponent},
 {path:'inicio',component:InicioComponent},
 {path:'contacto',component:ContactoComponent},
 {path:'registro',component:RegistroComponent},

 { path: '', redirectTo: 'login', pathMatch: 'full' },
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
