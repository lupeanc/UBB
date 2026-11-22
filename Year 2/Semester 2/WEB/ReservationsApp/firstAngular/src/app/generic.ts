import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http'

import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Reservation } from './reservation';
import { Room } from './room';
import { User } from './user';

@Injectable({
  providedIn: 'root',
})
export class GenericService {
  // CHANGE THIS TO THE CONTROLLER PF THE BACKEND
  // private backendUrl = 'http://localhost:8000/controller/Controller.php'
  private backendUrl = 'https://localhost:7175/'

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  };

  
  constructor(private http: HttpClient){}

  loginUser(username: string, password: string): Observable<any>{
    return this.http.get<string>(this.backendUrl+'?action=getUser&username='+username+'&password='+password)
    .pipe(catchError(this.handleError<string>('fetchUser')))
  }

  fetchReservations() : Observable<Reservation[]>{
    return this.http.get<Reservation[]>(this.backendUrl+'?action=getAllReservations')
            .pipe(catchError(this.handleError<Reservation[]>('fetchReservations', [])));
  }

  fetchRooms() : Observable<Room[]>{
  return this.http.get<Room[]>(this.backendUrl+'?action=getAllRooms')
          .pipe(catchError(this.handleError<Room[]>('fetchRooms', [])));
  }

  fetchReservation(id: number) : Observable<Reservation> {
    return this.http.get<Reservation>(this.backendUrl+'?action=getReservation&id=' + id)
          .pipe(catchError(this.handleError<Reservation>('fetchReservation')));
  }

    fetchRoom(id: number) : Observable<Room> {
    return this.http.get<Room>(this.backendUrl+'?action=getRoom&id=' + id)
          .pipe(catchError(this.handleError<Room>('fetchRoom')));
  }

  fetchNbBedsList() : Observable<number[]>{
    let url = `${this.backendUrl}?action=getNbBeds`;
    return this.http.get<number[]>(url)
            .pipe(catchError(this.handleError<number[]>('fetchNbBedsList', [])))
  }

  fetchCategories() : Observable<string[]>{
    let url = `${this.backendUrl}?action=getCategories`;
    return this.http.get<string[]>(url)
            .pipe(catchError(this.handleError<string[]>('fetchCategories', [])))
  }

  fetchPrices() : Observable<number[]>{
    let url = `${this.backendUrl}?action=getPrices`;
    return this.http.get<number[]>(url)
            .pipe(catchError(this.handleError<number[]>('fetchPrices', [])))
  }

  fetchFilteredRoomsByNbBeds(nbBeds:number) : Observable<Room[]>{
    let url = `${this.backendUrl}?action=getFilteredRoomsByNbBeds&nb_beds=${nbBeds}`;
    return this.http.get<Room[]>(url)
            .pipe(catchError(this.handleError<Room[]>('fetchFilteredRoomsByNbBeds', [])))
  }

  fetchFilteredRoomsByCategory(category:string) : Observable<Room[]>{
    let url = `${this.backendUrl}?action=getFilteredRoomsByCategory&category=${category}`;
    return this.http.get<Room[]>(url)
            .pipe(catchError(this.handleError<Room[]>('fetchFilteredRoomsByCategory', [])))
  }

  fetchFilteredRoomsByPrice(price:number): Observable<Room[]>{
  let url = `${this.backendUrl}?action=getFilteredRoomsByPrice&price=${price}`;
  return this.http.get<Room[]>(url)
          .pipe(catchError(this.handleError<Room[]>('fetchFilteredRoomsByPrice', [])))
}

  addReservation(reservation:Reservation): Observable<any>{
    let url = `${this.backendUrl}?action=addReservation&user_id=${reservation.user_id}&room_id=${reservation.room_id}&start=${reservation.start}&end=${reservation.end}`
    return this.http.get<string>(url)
          .pipe(catchError(this.handleError<string>('addReservation', "")));
  }

  updateReservation(reservation:Reservation): Observable<any>{
    let url = `${this.backendUrl}?action=updateReservation&id=${reservation.id}&user_id=${reservation.user_id}&room_id=${reservation.room_id}&start=${reservation.start}&end=${reservation.end}`
    return this.http.get<string>(url)
          .pipe(catchError(this.handleError<string>('updateReservation', "")));
  }

  deleteReservation(id: number): Observable<any>{
    let url = `${this.backendUrl}?action=deleteReservation&id=${id}`
    return this.http.get<string>(url)
          .pipe(catchError(this.handleError<string>('deleteReservation', "")));
  }

    /**
   * Handle Http operation that failed.
   * Let the app continue.
   * @param operation - name of the operation that failed
   * @param result - optional value to return as the observable result
   */
   private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      // TO DO: send the error to remote logging infrastructure
      console.error(error); // log to console instead
      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }
}
