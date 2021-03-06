import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AutofocusDirective } from './directives/auto-focus.directive';

@NgModule({
  declarations: [
    AutofocusDirective,
  ],
  imports: [
    CommonModule
  ],
  exports: [
    AutofocusDirective,
  ],
})
export class SharedModule { }
