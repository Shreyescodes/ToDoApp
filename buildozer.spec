[app]
# Title of your app
title = ToDoApp

# Unique identifier for your Android package (replace with your desired name)
package.name = com.example.ToDoApp

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ogg

# (list) List of inclusions using pattern matching
source.include_patterns = data/*.png, sound/*.ogg

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (str) Application versioning (method 1)
version = 0.1

# (str) Presplash of the application
presplash.filename = tickmark.png

# (str) Icon of the application
icon.filename = tickmark.png

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

author = © Shreyas 

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 2.3.0

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# (See https://python-for-android.readthedocs.io/en/latest/buildoptions.html for all the supported syntaxes and properties)
android.permissions = android.permission.INTERNET, android.permission.CAMERA, android.permissions.READ_EXTERNAL_STORAGE, android.permissions.WRITE_EXTERNAL_STORAGE,(name=android.permission.WRITE_EXTERNAL_STORAGE;maxSdkVersion=18)

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 23b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
#android.ndk_api = 21

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android SDK
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
# android.skip_update = False

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True


[buildozer]
# Requirements and other buildozer configurations
requirements = python3,sqlite3, kivy==2.1.0, https://github.com/kivymd/KivyMD/archive/master.zip,sdl2_ttf==2.0.15,pillow,android
