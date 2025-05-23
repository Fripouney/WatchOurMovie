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
    {
      path: 'films',
      loadComponent: () => import('./components/movies/movies.component').then(m => m.MoviesComponent),
    },
    {
      path: 'films/:id',
      loadComponent: () => import('./components/movie-details/movie-details.component').then(m => m.MovieDetailsComponent)
    },
    {
      path: 'friends',
      loadComponent: () => import('./components/friends/friends.component').then(m => m.FriendsComponent)
    },
    {
      path: 'watch',
      loadComponent: () => import('./components/watch/watch.component').then(m => m.WatchComponent)
    }
];
