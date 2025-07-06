import { Component } from '@angular/core';
import { MainView } from './main-view/main-view';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [MainView],
  template: '<app-main-view></app-main-view>',
})
export class App {
}
