import { Component, OnInit } from '@angular/core';
import { Reservation } from '../reservation';
import { GenericService } from '../generic';
import { CommonModule } from '@angular/common';
import { ChangeDetectorRef } from '@angular/core';

@Component({
  selector: 'app-reservations-crud',
  // standalone: true,
  imports: [CommonModule],
  templateUrl: './reservations-crud.html',
  styleUrl: './reservations-crud.css',
})
export class ReservationsCrud implements OnInit{
  reservations : Reservation[] = [];

    constructor(private genericService: GenericService, private cdr:ChangeDetectorRef){}

    ngOnInit(): void {
        this.getReservations();
    }

    getReservations(): void {
  // console.log("Fetching reservations...");
      this.genericService.fetchReservations()
        .subscribe(data => {
          console.log("DATA:", data);
          this.reservations = data;
          this.cdr.detectChanges();
        });
    }

    onUpdate(res: Reservation): void {
      (<HTMLInputElement>document.getElementById("id2")).value = String(res.id);
      (<HTMLInputElement>document.getElementById("user_id2")).value = String(res.user_id);
      (<HTMLInputElement>document.getElementById("room_id2")).value = String(res.room_id);
      (<HTMLInputElement>document.getElementById("start2")).value = (res.start);
      (<HTMLInputElement>document.getElementById("end2")).value = (res.end);
      
      let displayVal:string = document.getElementById('update_form')!.style.display;
      if (displayVal === "none")
        document.getElementById('update_form')!.style.display = "inline";
      else document.getElementById('update_form')!.style.display = "none";
      }

    onDelete(resId:number): void {
      this.genericService.deleteReservation(resId)
            .subscribe( r => {
              // console.log(r);
              alert(`Reservation ${resId} has been deleted!`)
              this.ngOnInit();
            });
    }

    addReservation(newUser_id: HTMLInputElement, newRoom_id:HTMLInputElement, newStart:HTMLInputElement, newEnd:HTMLInputElement){
      let addedReservation: Reservation = { id: 0,
        user_id: Number(newUser_id.value),
        room_id: Number(newRoom_id.value),
        start: newStart.value,
        end: newEnd.value
      };
      // console.log("ADDED:" + addedReservation.start + addedReservation.end)

      this.genericService.addReservation(addedReservation)
      .subscribe( r => {
        if(r.result=="Error"){
          alert("Reservation could not be added. Try again.")
        }
        else {
          alert("Reservation added succesfully!")
          this.ngOnInit();
        }
      });

      (<HTMLInputElement>document.getElementById("user_id1")).value = ' ';
      (<HTMLInputElement>document.getElementById("room_id1")).value = ' ';
      (<HTMLInputElement>document.getElementById("start1")).value = ' ';
      (<HTMLInputElement>document.getElementById("end1")).value = ' ';
    }

    updateReservation(uId: HTMLInputElement, uUser_id: HTMLInputElement, uRoom_id: HTMLInputElement, uStart: HTMLInputElement, uEnd: HTMLInputElement){
      let updatedReservation: Reservation = {id: + uId.value,
        user_id: Number(uUser_id.value),
        room_id: Number(uRoom_id.value),
        start: uStart.value,
        end: uEnd.value
      };

      this.genericService.updateReservation(updatedReservation)
            .subscribe(r =>{
              console.log(r.result);
              if(r.result=="Error"){
                alert("Reservation could not be updated. Try again.")
              }
              else {
                alert("Reservation updated succesfully!")
                document.getElementById('update_form')!.style.display = "none";
                this.ngOnInit();
              }         
            });

    }

}
