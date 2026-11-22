import { RouterModule, Routes } from '@angular/router';
import {ReservationsHome} from './reservations-home/reservations-home'
import { ReservationsCrud } from './reservations-crud/reservations-crud';
import { NgModule } from '@angular/core';
import { RoomsFilter } from './rooms-filter/rooms-filter';
import { Login } from './login/login';

export const routes: Routes = [
    {path:'', redirectTo: '/login', pathMatch: 'full'},
    {path: 'login', component: Login},
    {path: 'reservations-home', component: ReservationsHome},
    {path: 'reservations-crud', component: ReservationsCrud},
    {path: 'rooms-filter', component: RoomsFilter},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
