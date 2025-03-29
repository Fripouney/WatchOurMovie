import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import axios from 'axios';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './login.component.html',
})
export class LoginComponent {
  username = '';
  password = '';
  error = '';

  constructor(private router: Router) {}

  async login() {
    try {
      const response = await axios.post('http://localhost:8000/login', {
        username: this.username,
        password: this.password,
      });

      localStorage.setItem('token', response.data.access_token);
      this.router.navigate(['/']);
    } catch (err) {
      this.error = 'Identifiants incorrects';
    }
  }
}
