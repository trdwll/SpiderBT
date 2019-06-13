# TODO


## Immediate

- Full redesign as the current design is based off of Unreal Engine issues design
- Allow users to __[@username](#)__ to notify users or tag users
    - Simple API to request users that have posted a case for said product and staff of the product
    - jQuery keypress event?
- Allow users to [#_PN_-_ID_](#) to reference other cases (PN stands for the abbreviation of the ProductName)
    - Simple API to request cases that are equal to the case number that's put after the -
    - /api/v1/fetch/case/PN-ID
- Allow markdown in cases and notes
- Searching
- User disconnecting (oauth disconnection/delete all user data if they request)
    - This would delete their account, but rename the username on cases/casenotes to _Anonymous_.
- Add WYSIWYG editor for notes and cases
- Document code so other developers can understand the code easier
- Hide selected versions in patch_version if selected in affect_version
- Disabling registration via settings.py doesn't actually disable the oauth
___



## Future

- Make README pretty :)
- Notifications
    - Email
    - Local (similar to GitHub)
    - Settings to opt-out/in of/for specific notifications
- Discord bot to notify users/staff of a case that's been opened
- API to allow developers to build external applications
- Custom URLs for Django admin models (instead of SpiderBT&lowbar;_model_ would be _model_)
- Advanced searching 
    - Parse commands such as product:<ID/Title>, contains:"phrase", etc
- Add local authentication


___


## Possible

- Custom design for admin panel
    - http://themicon.co/theme/angle/v3.8.9/backend-jquery/app/bug-tracker.html
- Translations (either using Django or some jQuery lib)