import { Component } from '@angular/core';
import { Router } from '@angular/router';
import axios from 'axios';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  standalone: true,
  selector: 'app-register',
  templateUrl: './register.component.html',
  imports: [CommonModule, FormsModule, RouterModule]
})
export class RegisterComponent {
  username: string = '';
  password: string = '';
  confirmPassword: string = '';
  error: string = '';

  constructor(private router: Router) {}

  async register() {
    if (this.password !== this.confirmPassword) {
      this.error = 'Les mots de passe ne correspondent pas.';
      return; 
    }

    try {
      const response = await axios.post('http://localhost:8000/register', {
        username: this.username,
        password: this.password
      });

      const token = response.data.access_token;
      localStorage.setItem('token', token);
      this.router.navigate(['/']); // redirige vers l'accueil après inscription
    } catch (err: any) {
      if (err.response?.status === 400) {
        this.error = err.response.data.detail;
      } else {
        this.error = 'Une erreur est survenue. Veuillez réessayer.';
      }
    }
  }
}
