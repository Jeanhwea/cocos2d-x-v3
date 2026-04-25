LOCAL_PATH := $(call my-dir)
include $(CLEAR_VARS)

LOCAL_MODULE := spine4

LOCAL_MODULE_FILENAME := libspine4

LOCAL_ARM_MODE := arm

LOCAL_SRC_FILES := \
Animation.cpp \
AnimationState.cpp \
AnimationStateData.cpp \
Atlas.cpp \
AtlasAttachmentLoader.cpp \
Attachment.cpp \
AttachmentLoader.cpp \
AttachmentTimeline.cpp \
Bone.cpp \
BoneData.cpp \
BoundingBoxAttachment.cpp \
ClippingAttachment.cpp \
ColorTimeline.cpp \
ConstraintData.cpp \
CurveTimeline.cpp \
DeformTimeline.cpp \
DrawOrderTimeline.cpp \
Event.cpp \
EventData.cpp \
EventTimeline.cpp \
Extension.cpp \
IkConstraint.cpp \
IkConstraintData.cpp \
IkConstraintTimeline.cpp \
InheritTimeline.cpp \
Json.cpp \
LinkedMesh.cpp \
Log.cpp \
MathUtil.cpp \
MeshAttachment.cpp \
PathAttachment.cpp \
PathConstraint.cpp \
PathConstraintData.cpp \
PathConstraintMixTimeline.cpp \
PathConstraintPositionTimeline.cpp \
PathConstraintSpacingTimeline.cpp \
PhysicsConstraint.cpp \
PhysicsConstraintData.cpp \
PhysicsConstraintTimeline.cpp \
PointAttachment.cpp \
RTTI.cpp \
RegionAttachment.cpp \
RotateTimeline.cpp \
ScaleTimeline.cpp \
Sequence.cpp \
SequenceTimeline.cpp \
ShearTimeline.cpp \
Skeleton.cpp \
SkeletonAnimation.cpp \
SkeletonBatch.cpp \
SkeletonBinary.cpp \
SkeletonBounds.cpp \
SkeletonClipping.cpp \
SkeletonData.cpp \
SkeletonJson.cpp \
SkeletonRenderer.cpp \
SkeletonRendererCocos2dX.cpp \
SkeletonTwoColorBatch.cpp \
Skin.cpp \
Slot.cpp \
SlotData.cpp \
SpineObject.cpp \
TextureLoader.cpp \
Timeline.cpp \
TransformConstraint.cpp \
TransformConstraintData.cpp \
TransformConstraintTimeline.cpp \
TranslateTimeline.cpp \
Triangulator.cpp \
Updatable.cpp \
VertexAttachment.cpp \
spine-cocos2dx.cpp

LOCAL_EXPORT_C_INCLUDES := $(LOCAL_PATH)/..

LOCAL_C_INCLUDES := $(LOCAL_PATH)/..

LOCAL_STATIC_LIBRARIES := cc_core

include $(BUILD_STATIC_LIBRARY)
