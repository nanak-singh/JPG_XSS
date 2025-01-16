A vulnerability was identified in the application where the browser's "Back" button allows users to view previously accessed pages even after the user session has been terminated. This is primarily due to improper caching settings, leading to sensitive information potentially being exposed after logout.
Upon logging out of the application, the browser cache retains previously accessed pages. When a user clicks the "Back" button, the cached pages are displayed without re-authentication. Although actions on these pages may not be possible due to session invalidation, the exposure of sensitive information increases the risk of unauthorized access.

 it is essential to implement proper cache control mechanisms. This includes adding HTTP headers like Cache-Control: no-cache, no-store, must-revalidate, Pragma: no-cache, and Expires: 0 to all sensitive pages to prevent browsers from caching them. Additionally, ensure that session validation checks are in place for all server responses, denying access to pages if the session is invalidated. A forced page reload or redirection upon logout can also help clear cached content. Regular testing across multiple browsers should be conducted to verify that caching vulnerabilities are fully mitigated. These measures will ensure sensitive information is not exposed and bolster the security of user sessions.


Reproduction Steps
Login to the application using valid credentials.
Navigate through several pages with sensitive data.
Logout of the application.
Use the browser's "Back" button to navigate to previously accessed pages.
Observe that the sensitive information is visible without being prompted for re-authentication.
