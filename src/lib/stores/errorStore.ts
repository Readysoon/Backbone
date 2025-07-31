
import { writable } from "svelte/store"

export type ErrorType = {
    message: string | null;
    type: string | null;
    code: string | number | null;
    details: any;
  };

  
  export const globalError = writable<ErrorType>({
    message: null,
    type: null,
    code: null,
    details: null
  });
  
  export function setError({ message = null, type = null, code = null, details = null }: Partial<ErrorType>) {
    globalError.set({ message, type, code, details });
  }
  
  export function clearError() {
    globalError.set({ message: null, type: null, code: null, details: null });
  }