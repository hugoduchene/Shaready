import { infinite, create_loader } from './module/settings.js'
import { manage_notification } from './module/settings_notification.js'

/* display first page of notification */
manage_notification(1)

/* infinite scroll */

const item = document.getElementById('end_body')
infinite(item, manage_notification)


