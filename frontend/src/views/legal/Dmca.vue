<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">

    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="bg-white shadow-lg rounded-lg p-6 space-y-8">
        <div class="text-center">
          <h1 class="text-3xl font-bold text-gray-900">DMCA Takedown Policy</h1>
          <p class="text-gray-600 mt-2">Copyright Infringement Notification Process</p>
        </div>

        <div class="bg-blue-50 p-4 rounded-lg border border-blue-200">
          <div class="flex items-start space-x-3">
            <AlertCircle class="h-6 w-6 text-blue-600 mt-1 flex-shrink-0" />
            <div>
              <h3 class="font-semibold text-blue-900 mb-1">Important Notice</h3>
              <p class="text-blue-800 text-sm">
                If you believe that any content posted on ReviewGallery infringes your copyright,
                you may submit a DMCA takedown notice to request the removal of that content.
              </p>
            </div>
          </div>
        </div>

        <section>
          <h3 class="text-xl font-semibold text-gray-900 mb-3 flex items-center">
            <Mail class="h-5 w-5 mr-2 text-indigo-600" />
            How to File a DMCA Notice
          </h3>
          <p class="text-gray-700 mb-4">
            To file a notice, please email us at <strong>dmca@reviewgallery.com</strong> with the following details:
          </p>
        </section>

        <div class="bg-gray-50 rounded-lg p-4 space-y-4">
          <div class="flex items-center mb-2">
            <FileText class="h-5 w-5 mr-2 text-gray-700" />
            <h3 class="text-lg font-semibold text-gray-900">DMCA Takedown Request Template</h3>
          </div>

          <div class="space-y-3 text-sm">
            <div>
              <span class="font-medium text-gray-900">Your Full Name:</span>
              <div class="border-b border-gray-300 mt-1 pb-1"></div>
            </div>

            <div>
              <span class="font-medium text-gray-900">Your Contact Email:</span>
              <div class="border-b border-gray-300 mt-1 pb-1"></div>
            </div>

            <div>
              <span class="font-medium text-gray-900">Your Company (if applicable):</span>
              <div class="border-b border-gray-300 mt-1 pb-1"></div>
            </div>

            <div>
              <span class="font-medium text-gray-900">Description of the copyrighted work:</span>
              <div class="border-b border-gray-300 mt-1 pb-1"></div>
            </div>

            <div>
              <span class="font-medium text-gray-900">URL(s) of the infringing content:</span>
              <div class="border-b border-gray-300 mt-1 pb-1"></div>
            </div>
          </div>

          <hr class="border-gray-300" />

          <div class="space-y-3">
            <div>
              <span class="font-medium text-gray-900">Statement:</span>
              <p class="text-gray-700 text-sm mt-1 italic">
                "I have a good faith belief that the use of the copyrighted material described above
                is not authorized by the copyright owner, its agent, or the law."
              </p>
            </div>

            <div>
              <span class="font-medium text-gray-900">Statement (under penalty of perjury):</span>
              <p class="text-gray-700 text-sm mt-1 italic">
                "I swear, under penalty of perjury, that the information in this notification is accurate
                and that I am the copyright owner or authorized to act on behalf of the copyright owner."
              </p>
            </div>

            <div>
              <span class="font-medium text-gray-900">Your Signature (typed name is acceptable):</span>
              <div class="border-b border-gray-300 mt-1 pb-1"></div>
            </div>
          </div>
        </div>

        <section>
          <h3 class="text-xl font-semibold text-gray-900 mb-2">Processing Your Request</h3>
          <p class="text-gray-700">
            We will review all DMCA takedown requests promptly and take appropriate action in accordance with
            the Digital Millennium Copyright Act. Invalid or incomplete requests may be rejected.
          </p>
        </section>

        <section>
          <h3 class="text-xl font-semibold text-gray-900 mb-2">Contact Information</h3>
          <p class="text-gray-700">
            DMCA Agent: ReviewGallery Legal Team<br />
            Email: dmca@reviewgallery.com<br />
            Response Time: 24-72 hours
          </p>
        </section>
      </div>
    </div>
  </div>
</template>

<script setup>

import { Mail, FileText, AlertCircle } from 'lucide-vue-next'
</script>
