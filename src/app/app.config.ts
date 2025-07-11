import { ApplicationConfig, provideZoneChangeDetection, importProvidersFrom } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { provideAnimations } from '@angular/platform-browser/animations';
import { QuillModule } from 'ngx-quill';
import { HammerModule, HammerGestureConfig, HAMMER_GESTURE_CONFIG } from '@angular/platform-browser';

import { routes } from './app.routes';
import { registerQuillBlots } from './core/quill/quill.config';

// Register custom Quill blots
registerQuillBlots();

declare const Hammer: any; // Declare Hammer to avoid TypeScript errors

export class CustomHammerConfig extends HammerGestureConfig {
  override buildHammer(element: HTMLElement) {
    const mc = new Hammer(element, {
      touchAction: 'pan-y', // Allow vertical scrolling, but enable horizontal pan
    });

    // Recognize horizontal pan gestures
    mc.get('pan').set({ direction: Hammer.DIRECTION_HORIZONTAL });

    return mc;
  }
}

export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes),
    provideHttpClient(),
    provideAnimations(),
    importProvidersFrom(QuillModule.forRoot(), HammerModule),
    { provide: HAMMER_GESTURE_CONFIG, useClass: CustomHammerConfig }
  ]
};
