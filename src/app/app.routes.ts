import { Routes } from '@angular/router';
import { MainView } from './main-view/main-view';
import { DescriptionPage } from './description-page/description-page';

export const routes: Routes = [
    { path: '', component: MainView },
    { path: 'description/:stockTicker/:listCode', component: DescriptionPage },
];
