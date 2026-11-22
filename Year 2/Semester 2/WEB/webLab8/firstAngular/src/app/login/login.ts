import { Component, OnInit } from '@angular/core';
import { GenericService } from '../generic';
import { RedirectCommand } from '@angular/router';

@Component({
  selector: 'app-login',
  imports: [],
  templateUrl: './login.html',
  styleUrl: './login.css',
})
export class Login implements OnInit{

  constructor(private genericService: GenericService){}

  ngOnInit(): void {
    
  }

  login(username:HTMLInputElement, password: HTMLInputElement):void{
    let usernameString:string = username.value;
    let passwordString:string = password.value;
    this.genericService.loginUser(usernameString, passwordString)
        .subscribe(r =>{
          if(r.result=="Error"){
            alert("Could not log in. Try again!");
          }
          else{
            alert("Welcome to Reservations!")
            window.location.href="/reservations-home"
          }
        }

        )
  }

}
