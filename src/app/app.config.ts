import { ApplicationConfig, provideZoneChangeDetection, importProvidersFrom } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { provideAnimations } from '@angular/platform-browser/animations';
import { QuillModule } from 'ngx-quill';
import { HammerModule } from '@angular/platform-browser';

import { routes } from './app.routes';
import { registerQuillBlots } from './core/quill/quill.config';

// Register custom Quill blots
registerQuillBlots();

export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes),
    provideHttpClient(),
    provideAnimations(),
    importProvidersFrom(QuillModule.forRoot(), HammerModule)
  ]
};
