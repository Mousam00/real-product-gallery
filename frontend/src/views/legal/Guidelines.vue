<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">

    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="bg-white shadow-lg rounded-lg p-6 space-y-6">
        <div class="text-center">
          <h1 class="text-3xl font-bold text-gray-900">Community Comment Guidelines</h1>
          <p class="text-gray-600 mt-2">Keep ReviewGallery a helpful and positive space</p>
        </div>

        <p class="text-gray-700">
          To keep ReviewGallery a helpful and positive space, please follow these simple rules when commenting on images or posts:
        </p>

        <div class="grid md:grid-cols-2 gap-6">
          <div class="flex items-start space-x-3">
            <Heart class="h-6 w-6 text-red-500 mt-1" />
            <div>
              <h3 class="font-semibold text-gray-900 mb-1">Be Respectful</h3>
              <p class="text-gray-700 text-sm">
                Treat others with kindness and respect. No personal attacks, hate speech, or harassment.
              </p>
            </div>
          </div>

          <div class="flex items-start space-x-3">
            <MessageCircle class="h-6 w-6 text-blue-500 mt-1" />
            <div>
              <h3 class="font-semibold text-gray-900 mb-1">Stay Relevant</h3>
              <p class="text-gray-700 text-sm">
                Keep your comments related to the product, image, or discussion topic.
              </p>
            </div>
          </div>

          <div class="flex items-start space-x-3">
            <Shield class="h-6 w-6 text-green-500 mt-1" />
            <div>
              <h3 class="font-semibold text-gray-900 mb-1">No Offensive Content</h3>
              <p class="text-gray-700 text-sm">
                Don't post content that's abusive, obscene, illegal, or promotes violence.
              </p>
            </div>
          </div>

          <div class="flex items-start space-x-3">
            <Flag class="h-6 w-6 text-orange-500 mt-1" />
            <div>
              <h3 class="font-semibold text-gray-900 mb-1">No Spam or Promotions</h3>
              <p class="text-gray-700 text-sm">
                Avoid posting unsolicited ads, promotions, or links to unrelated products or services.
              </p>
            </div>
          </div>
        </div>

        <div class="border-t border-gray-200 pt-6 space-y-4">
          <section>
            <h3 class="text-xl font-semibold text-gray-900 mb-2">Report Issues</h3>
            <p class="text-gray-700">
              If you see inappropriate content or behavior, use the report button or contact us at moderation@reviewgallery.com
            </p>
          </section>

          <section>
            <h3 class="text-xl font-semibold text-gray-900 mb-2">Moderation Rights</h3>
            <p class="text-gray-700">
              ReviewGallery reserves the right to remove comments that violate these guidelines or our Terms of Service without notice.
            </p>
          </section>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { Heart, Flag, Shield, MessageCircle } from 'lucide-vue-next'
</script>
