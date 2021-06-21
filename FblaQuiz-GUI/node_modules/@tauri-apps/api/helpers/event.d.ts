/**
 * Emits an event to the backend.
 *
 * @param event Event name
 * @param [windowLabel] The label of the window to which the event is sent, if null/undefined the event will be sent to all windows
 * @param [payload] Event payload
 * @returns
 */
declare function emit(event: string, windowLabel?: string, payload?: string): Promise<void>;
export { emit };
