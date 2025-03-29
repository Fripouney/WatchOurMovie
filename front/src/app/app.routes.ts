import { Routes } from '@angular/router';

export const routes: Routes = [
    {
      path: '',
      loadComponent: () => import('./components/home/home.component').then(m => m.HomeComponent),
    },
    {
      path: 'profil',
      loadComponent: () => import('./components/profil/profil.component').then(m => m.ProfilComponent),
    },
    {
      path: 'login',
      loadComponent: () => import('./components/login/login.component').then(m => m.LoginComponent),
    },
    {
      path: 'register',
      loadComponent: () => import('./components/register/register.component').then(m => m.RegisterComponent),
    },
];
