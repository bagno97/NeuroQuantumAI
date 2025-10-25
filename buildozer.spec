[app]

# Application metadata
title = NeuroQuantumAI
package.name = neuroquantumai
package.domain = org.bagno97

# Source files
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

# Application version
version = 1.0.0

# Requirements: include core and Android-specific packages
# Dostosuj listę jeśli twoje requirements.txt zawiera inne biblioteki
requirements = python3,kivy,plyer,requests,flask,numpy,pyjnius,python-for-android

# Orientation
orientation = portrait

# Permissions required for phone features
android.permissions = INTERNET,CAMERA,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,SEND_SMS,READ_SMS,RECEIVE_SMS,CALL_PHONE,READ_PHONE_STATE,ACCESS_WIFI_STATE,CHANGE_WIFI_STATE,BLUETOOTH,BLUETOOTH_ADMIN,VIBRATE,WAKE_LOCK

# Android features
android.features = android.hardware.camera,android.hardware.location.gps

# Android API/NDK settings
android.api = 33
android.minapi = 21
android.ndk = 25b

# Architectures
android.archs = arm64-v8a,armeabi-v7a

# Use SDL2 bootstrap for Kivy
p4a.bootstrap = sdl2

# Packaging options
android.release_artifact = apk

# Logging
log_level = 2
warn_on_root = 1

[buildozer]

log_level = 2
warn_on_root = 1
